import logging
import feedparser
import asyncio
import re

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración del bot
TOKEN = "7528210835:AAHG-L-1xuv_xK-UBaWRxM0ySE9tNBHflh8"
NEWS_FEED_URL = "https://rss.app/feeds/CgegXHpAPvk6jVH3.xml"
GROUP_CHAT_ID = -4624834551
MAX_MESSAGE_LENGTH = 4096

# Almacenar noticias enviadas para evitar duplicados
sent_articles = set()

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def escape_markdown(text):
    """Escapa caracteres especiales para MarkdownV2 en Telegram"""
    escape_chars = r"_*[]()~`>#+-=|{}.!<>"
    # Primero, reemplaza las barras invertidas existentes para evitar doble escape
    text = text.replace("\\", "\\\\")
    # Luego, escapa los demás caracteres especiales
    return re.sub(r"([%s])" % re.escape(escape_chars), r"\\\1", text)


# Función para obtener noticias
def get_latest_news():
    feed = feedparser.parse(NEWS_FEED_URL)
    articles = []
    
    for entry in feed.entries:
        title = escape_markdown(entry.title)  # Escapar caracteres especiales
        link = entry.link
        if link not in sent_articles:
            sent_articles.add(link)
            articles.append(f"📰 *{title}*\n🔗 {link}")
    
    return articles

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"El chat_id de este grupo es: {chat_id}")

async def news_loop(application: Application):
    job_queue = application.job_queue

    for job in job_queue.jobs():
        job.schedule_removal()  # Eliminar tareas anteriores

    job_queue.run_repeating(send_news, interval=600, first=5)  # Enviar cada 10 min
    await asyncio.sleep(600)  # Esperar 10 min antes de reprogramar


# Enviar noticias nuevas
async def send_news(context: ContextTypes.DEFAULT_TYPE):
    news = get_latest_news()

    for article in news:
        article = escape_markdown(article)  # Escapa caracteres
        try:
            await context.bot.send_message(chat_id=GROUP_CHAT_ID, text=article, parse_mode="MarkdownV2")
        except Exception as e:
            logging.error(f"Error al enviar mensaje: {e}")

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
    
    application.add_handler(CommandHandler("getid", get_chat_id))  # Comando para obtener el chat_id del grupo

    loop = asyncio.get_event_loop()
    loop.create_task(news_loop(application))  # Iniciar la verificación de noticias

    application.run_polling()


if __name__ == "__main__":
    main()
