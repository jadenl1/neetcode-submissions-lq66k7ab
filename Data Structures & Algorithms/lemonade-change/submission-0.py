class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket = {5: 0, 10: 0, 20: 0}

        for i, bill in enumerate(bills):
            pocket[bill] += 1
            change = bill - 5

            print(pocket)
            print(i, 'bill: ', bill)
            print('change: ', change)
            print('...........')

            if change == 5:
                if pocket[5] == 0:
                    return False
                pocket[5] -= 1
            elif change == 15:
                if pocket[5] >= 3:
                    pocket[5] -= 3
                elif pocket[5] >= 1 and pocket[10] >= 1:
                    pocket[5] -= 1
                    pocket[10] -= 1
                else:
                    return False
        
        return True
