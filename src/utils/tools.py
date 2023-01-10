def auto_chunking(text: str, chunk_length: int):
  return [text[i:i+chunk_length] for i in range(0, len(text), chunk_length)]