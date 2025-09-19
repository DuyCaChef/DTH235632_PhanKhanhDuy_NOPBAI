def oscillate(start, end):
    # In ra start trước
    yield start
    # Sau đó tạo dao động từ start đến end-1
    for i in range(start, end):
        yield i
        yield -i
for n in oscillate(-3, 5):
    print(n, end=' ')
