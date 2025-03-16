import logging
import feedparser
import asyncio

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración del bot
TOKEN = "7528210835:AAHG-L-1xuv_xK-UBaWRxM0ySE9tNBHflh8"
NEWS_FEED_URL = "https://rss.app/feeds/CgegXHpAPvk6jVH3.xml"

# Almacenar noticias enviadas para evitar duplicados
sent_articles = set()

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Función para obtener noticias
def get_latest_news():
    feed = feedparser.parse(NEWS_FEED_URL)
    articles = []
    
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        if link not in sent_articles:  # Verificar si ya se envió
            sent_articles.add(link)
            articles.append(f"📰 *{title}*\n🔗 {link}")
    
    return articles

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Te enviaré noticias de tecnología automáticamente.")

# Enviar noticias nuevas
async def send_news(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id  # Obtener el chat donde se ejecutó /start
    news = get_latest_news()
    
    for article in news:
        await context.bot.send_message(chat_id=chat_id, text=article, parse_mode="Markdown")

# Configurar verificación automática cada 10 min
async def news_loop(application: Application):
    while True:
        job_queue = application.job_queue
        for job in job_queue.jobs():
            job.schedule_removal()  # Eliminar tareas anteriores

        job_queue.run_repeating(send_news, interval=600, first=5)
        await asyncio.sleep(600)  # Esperar 10 min antes de reprogramar

# Iniciar bot
def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    # Ejecutar la verificación de noticias en segundo plano dentro del loop correcto
    loop = asyncio.get_event_loop()
    loop.create_task(news_loop(application))

    application.run_polling()  # Mantiene el bot en ejecución

if __name__ == "__main__":
    main()
