from llama_index.core import Document
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

# 创建Document对象
doc = Document(text=text)

# 使用tiktoken计算tokens
encoding = tiktoken.get_encoding("cl100k_base")  # 这是GPT-4使用的编码器
tokens = encoding.encode(text)
total_tokens = len(tokens)

print(f"\nLlamaIndex Document + Tiktoken计算结果:")
print(f"Token数量: {total_tokens}")
if total_tokens > 512:
    print(f"超过512个tokens！超出了 {total_tokens - 512} 个tokens")
else:
    print(f"未超过512个tokens，还可以添加 {512 - total_tokens} 个tokens")

# 显示详细的token信息
print("\n详细信息:")
print(f"文本长度: {len(text)} 字符")
print(f"平均每个token包含 {len(text)/total_tokens:.2f} 个字符")

# 显示前10个tokens的解码结果
print("\n前10个tokens的解码结果:")
for i, token in enumerate(tokens[:10]):
    print(f"Token {i+1}: {encoding.decode([token])!r}") 