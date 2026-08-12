from rag_pipeline import ask


question = "What is Ahmed's department, job title, and joining date?"

answer, sources = ask(question)

print("\nEmployee Information:")
print(answer)

print("\nSource:")
for source in sources:
    print("-", source)