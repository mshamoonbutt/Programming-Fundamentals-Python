def calculate_mean(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    mean = total / count
    return mean

def main():
    try:
        with open('test.in', 'r') as file:
            n = int(file.readline().strip())
            scores = []
            for _ in range(n):
                score = int(file.readline().strip())
                scores.append(score)

        mean = calculate_mean(scores)
        print(f'Mean: {mean}')
    except FileNotFoundError:
        print('Error: File test.in not found.')

if __name__ == "__main__":
    main()