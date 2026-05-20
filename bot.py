from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# এখানে তোমার Bot Token বসাও
BOT_TOKEN = "8801340067:AAHfr7kYq_wBP1dzbtgP8XRI2xi8B45LYS0"


# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.first_name

    text = f"""
╔══❖•ೋ° 🌸 °ೋ•❖══╗
      🤖 হেল্প সেন্টার বট
╚══❖•ೋ° 🌸 °ೋ•❖══╝

👋 আসসালামু আলাইকুম {user}

আমি একটি Telegram Help Bot ✅

এখান থেকে আপনি জানতে পারবেনঃ

📌 বটের সকল কমান্ড
📌 GitHub এ Upload System
📌 Render Hosting Guide
📌 24/7 Bot Hosting
📌 Owner Support

নিচের বাটনগুলো ব্যবহার করুন 👇
"""

    keyboard = [
        [
            InlineKeyboardButton("📚 সকল কমান্ড", callback_data="commands")
        ],
        [
            InlineKeyboardButton("🌐 Hosting Guide", callback_data="hosting")
        ],
        [
            InlineKeyboardButton("💻 GitHub System", callback_data="github")
        ],
        [
            InlineKeyboardButton("🆘 সাপোর্ট", callback_data="support")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )


# বাটন সিস্টেম
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # Commands
    if data == "commands":

        text = """
╔══❖•ೋ° 📚 °ೋ•❖══╗
        সকল কমান্ড
╚══❖•ೋ° 📚 °ೋ•❖══╝

/start - বট চালু করুন
/help - সাহায্য দেখুন
/ping - বট অনলাইন কিনা দেখুন
/about - বট সম্পর্কে জানুন

✅ আরো নতুন ফিচার শীঘ্রই আসবে
"""

    # Hosting
    elif data == "hosting":

        text = """
╔══❖•ೋ° 🌐 °ೋ•❖══╗
      Hosting Guide
╚══❖•ೋ° 🌐 °ೋ•❖══╝

✅ GitHub এ কোড আপলোড করুন

✅ Render এ GitHub Connect করুন

✅ Background Worker Select করুন

✅ Deploy Button চাপুন

🚀 আপনার বট 24/7 অনলাইন থাকবে
"""

    # GitHub
    elif data == "github":

        text = """
╔══❖•ೋ° 💻 °ೋ•❖══╗
      GitHub System
╚══❖•ೋ° 💻 °ೋ•❖══╝

1️⃣ GitHub এ Repository তৈরি করুন

2️⃣ bot.py Upload করুন

3️⃣ requirements.txt Upload করুন

4️⃣ Render এ Deploy করুন

✅ Done Successfully 🚀
"""

    # Support
    elif data == "support":

        text = """
╔══❖•ೋ° 🆘 °ೋ•❖══╗
         Support
╚══❖•ೋ° 🆘 °ೋ•❖══╝

👨‍💻 Owner : @YourUsername

📩 কোন সমস্যা হলে Owner কে মেসেজ করুন

ধন্যবাদ ❤️
"""

    await query.message.reply_text(text)


# /help কমান্ড
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📌 Help Menu দেখতে /start ব্যবহার করুন"
    )


# /ping কমান্ড
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🏓 Bot বর্তমানে অনলাইনে আছে ✅"
    )


# /about কমান্ড
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 Bot Information

📌 বাংলা Telegram Help Bot
📌 তৈরি করা হয়েছে Python দিয়ে
📌 Hosting : Render
📌 Source : GitHub

🚀 Fast & Simple Bot
"""

    await update.message.reply_text(text)


# MAIN SYSTEM
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("about", about))

app.add_handler(CallbackQueryHandler(buttons))

print("✅ Bot Running Successfully...")

# Bot Start
app.run_polling()
