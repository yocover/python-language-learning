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

# 计算总字符数（包括空格和换行符）
total_chars = len(text)

# 计算不包括空格和换行符的字符数
chars_no_whitespace = len(text.replace(" ", "").replace("\n", ""))

# 计算不包括HTML注释标记的字符数
content = text.replace("<!--", "").replace("-->", "")
content_chars = len(content)

print(f"总字符数（包括所有字符）: {total_chars}")
print(f"不包括空格和换行符的字符数: {chars_no_whitespace}")
print(f"不包括HTML注释标记的内容字符数: {content_chars}")

# 检查是否超过512个字符
if total_chars > 512:
    print(f"\n超过512个字符！超出了 {total_chars - 512} 个字符")
else:
    print(f"\n未超过512个字符，还可以添加 {512 - total_chars} 个字符") 