from transformers import GPT2TokenizerFast
import tiktoken

text = """<!--
Hassan S. Alhazmi",
      "Eng. Badr S. AL-maayof",
      "Eng. Fayez A. Alghamdi",
      "Eng. Mohammed A. Afwaily",
      "Dr. Bandar S. Alkhalan",
      "Eng. Ahmad N. Hassan",
      "Eng. Abdunasser S. Alabdullatif",
      "Dr. Hani M. Zahran",
      "Eng. Khalifa S. Alyahyai",
      "Dr. Khaled M. Aljamamz",
      "Dr. Ibrahim O. Habiballah",
      "Dr. Saeed A. Asiri",
      "Dr. Abdallah M. Al-Shehri",
      "Eng. Saad S. Shuail"
    ]
  },
  "Advisory Committee": {
    "Chairman": "Dr. Khaled M. Aljamamz",
    "Vice Chairman": "Eng. Khalifa S. Alyahyai",
    "Members": [
      "Dr. Hani M. Zahran",
      "Prof. Ali A. Shash",
      "Prof. Ahmed B. Shuraim",
      "Dr. Khalid M. Wazira",
      "Dr. Abdulhameed A. Al Ohaly",
      "Dr. Hamza A. Ghulman",
      "Eng. Hakam A. Al-Aqily",
      "Prof. Saleh F. Magram",
      "Eng. Nasser M. Al-Dossari",
      "Dr. Walced H. Khushefati",
      "Dr. Waleed M. Abanomi",
      "Dr. Fahad S. Al-Lahaim"
    ]
  },
  "Reviewers": [
    "Dr. Ayman G.",
    "Engr. Kok-Wah Tung",
    "Abdual Rahman"
  ],
  "Editorial Committee": {
    "Chairman": "Prof. Ahmed B. Shuraim",
    "Members": [
      "Dr.
-->"""

def count_tokens_gpt2():
    """使用GPT2分词器计算token数"""
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    tokens = tokenizer.encode(text)
    return len(tokens)

def count_tokens_tiktoken():
    """使用tiktoken（OpenAI官方分词器）计算token数"""
    encoding = tiktoken.get_encoding("cl100k_base")  # GPT-4使用的编码器
    tokens = encoding.encode(text)
    return len(tokens)

try:
    # 使用tiktoken（OpenAI官方分词器）
    tiktoken_count = count_tokens_tiktoken()
    print(f"\nOpenAI tiktoken分词器计算结果:")
    print(f"Token数量: {tiktoken_count}")
    if tiktoken_count > 512:
        print(f"超过512个tokens！超出了 {tiktoken_count - 512} 个tokens")
    else:
        print(f"未超过512个tokens，还可以添加 {512 - tiktoken_count} 个tokens")
except Exception as e:
    print(f"tiktoken计算出错: {str(e)}")

try:
    # 使用GPT2分词器
    gpt2_count = count_tokens_gpt2()
    print(f"\nGPT2分词器计算结果:")
    print(f"Token数量: {gpt2_count}")
    if gpt2_count > 512:
        print(f"超过512个tokens！超出了 {gpt2_count - 512} 个tokens")
    else:
        print(f"未超过512个tokens，还可以添加 {512 - gpt2_count} 个tokens")
except Exception as e:
    print(f"GPT2计算出错: {str(e)}") 