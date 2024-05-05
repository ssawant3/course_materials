class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0
    def Count(self):
        self.comparison_count=self.comparison_count+1
        return True

    def merge_sort(self, p, r):
        if p<r:
            mid=int((p+r)/2)
            self.merge_sort(p,mid)
            self.merge_sort(mid+1,r)
            self.merge(self.sorting_array,p,r,mid)

        pass

    def heap_sort(self):
        for i in range(len(self.sorting_array)//2 - 1, -1, -1):
            self.maxheapify(self.sorting_array, len(self.sorting_array), i)
 
        for j in range(len(self.sorting_array)-1, 0, -1):
            self.sorting_array[j], self.sorting_array[0] = self.sorting_array[0], self.sorting_array[j]  
            self.maxheapify(self.sorting_array, j, 0)
        
        pass

    def insertion_sort(self):
        for i in range(1,len(self.sorting_array)):
            temp_element=self.sorting_array[i]
            j=i-1
            while j>=0 and self.Count() and self.sorting_array[j]>temp_element:
                self.sorting_array[j+1]=self.sorting_array[j]
                j=j-1
            self.sorting_array[j+1]=temp_element


    def maxheapify(self,arr,heapSize,par):
        left=2*par+1
        right=2*par+2
        largest=par
        if left<heapSize and self.Count() and arr[par]<arr[left]:
            largest=left
        if right<heapSize and self.Count() and arr[largest]<arr[right]:
            largest=right
        if par!=largest:
            arr[par], arr[largest]=arr[largest], arr[par]
            self.maxheapify(arr,heapSize,largest)    
    
    def merge(self,arr,start,end,middle):
        left=[0]*(middle-start+1)
        right=[0]*(end-middle)
        i=start 
        j=0
        k=0
        for m in range(middle-start+1):
            left[m]=arr[start+m]
        for n in range(end-middle):
            right[n]=arr[middle+1+n]
        
        while(j< len(left) and k<len(right)):
            if(self.Count() and left[j]<=right[k] ):
                arr[i]=left[j]
                j+=1
            else:
                arr[i]=right[k]
                k+=1
            i+=1

        while j<len(left):
            arr[i]=left[j]
            j+=1
            i+=1

        while j<len(right):
            arr[i]=right[k]
            k+=1
            i+=1
c1=Sorting([1, 2,3,4])
c1.heap_sort()
print("heap",c1.comparison_count,c1.sorting_array) 
c2=Sorting([1, 2,3,4])
c2.insertion_sort()
print("insertion",c2.comparison_count,c2.sorting_array)
c3=Sorting([3,6,1,9,34])
c3.merge_sort(0,2)
print("merge",c3.comparison_count,c3.sorting_array)