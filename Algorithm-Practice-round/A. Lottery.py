lucky = [int(n) for n in input().split()]
tickets = [[int(n) for n in input().split()] for ticket_number in range(int(input()))]
[print(res) for res in list(map(lambda res: 'Lucky' if res >= 3 else 'Unlucky', map(lambda ticket: len(list(filter(lambda num: num in lucky, ticket))), tickets)))]