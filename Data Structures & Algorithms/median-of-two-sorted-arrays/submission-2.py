class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l+r) // 2 # A
            j = half - i - 2 # B, j is index of mid point: subtract i and 2 to fix off by one errors since j and i start at 0

            # check correct left/right partition
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if i + 1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if j < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright: # correct partition
                if total % 2 == 0: # even case
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else: 
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1 # reduce left partition size
            else:
                l = i + 1 # increase size of left partition

