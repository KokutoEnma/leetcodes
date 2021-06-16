class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        direction drived
        """

#         min_x, min_y, max_x, max_y = 0, 0, len(matrix[0])-1, len(matrix)-1

#         i = j = 0
#         dir = 0
#         ret = []

#         while i>=min_x and i<=max_x and j>=min_y and j<=max_y:
#             ret.append(matrix[j][i])

#             if dir==0:
#                 if i==max_x:
#                     dir=1
#                     j+=1
#                     min_y+=1
#                 else: i+=1
#             elif dir==1:
#                 if j==max_y:
#                     dir=2
#                     i-=1
#                     max_x-=1
#                 else: j+=1
#             elif dir==2:
#                 if i==min_x:
#                     dir=3
#                     j-=1
#                     max_y-=1
#                 else: i-=1
#             else:
#                 if j==min_y:
#                     dir=0
#                     i+=1
#                     min_x+=1
#                 else: j-=1

#         return ret

        """
        layer by layer
        """
        min_x, min_y, max_x, max_y = 0, 0, len(matrix[0])-1, len(matrix)-1

        ret = []

        while min_x <= max_x and min_y <= max_y:
            for i in range(min_x, max_x+1):
                ret.append(matrix[min_y][i])
            for i in range(min_y+1, max_y+1):
                ret.append(matrix[i][max_x])

            if min_x < max_x and min_y < max_y:
                for i in range(max_x-1, min_x-1, -1):
                    ret.append(matrix[max_y][i])
                for i in range(max_y-1, min_y, -1):
                    ret.append(matrix[i][min_x])

            min_x += 1
            max_x -= 1
            min_y += 1
            max_y -= 1

        return ret
