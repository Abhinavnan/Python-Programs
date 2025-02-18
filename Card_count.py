'''
You are given a deck of cards. Each card has a number written on it. You have to pick cards from the deck.
The condition is that you can only pick a card if the sum of the numbers on the cards you have picked is non-negative.
You have to find the maximum number of cards you can pick.
'''

def card_count(start, end, cards, sum, count):
    if start == end:
        return count
    elif sum + cards[start] >= 0:
        sum += cards[start]
        count += 1
        return card_count(start+1, end, cards, sum, count)
    else:
        sum = sum + cards[start]
        deficit = sum 
        j = int(0)
        while j <= start:
            if cards[j] < deficit:
                deficit = cards[j]
            j += 1
        sum = sum - deficit 
        return card_count(start+1, end, cards, sum, count)
            
    
n = input("Enter the number of cards: ")
n = int(n)
cards = input("Enter the cards: ").split()[:n] # List of cards upto n
cards = [int(i) for i in cards] # Convert the list of strings to list of integers

result = card_count(0, n, cards, 0, 0)
print(result)



