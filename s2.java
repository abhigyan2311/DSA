class Solution 
{
    long colosseum(int N,int A[]) {
        int n=3*N; //length of A
        
        //calculate sum of N max values from left side
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        long [] leftSum= new long [n];
        long sum=0;
        for(int i=0;i<(2*N);i++){
            minHeap.offer(A[i]);
            sum+=A[i];
            if(minHeap.size()>N){
                sum-=minHeap.poll();
            }
            leftSum[i]=sum;
        }
        
        //calculate sum of N min values from right side
        sum=0;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        long [] rightSum= new long [n];
        for(int i=(n-1);i>=0;i--){
            maxHeap.offer(A[i]);
            sum+=A[i];
            if(maxHeap.size()>N){
                sum-=maxHeap.poll();
            }
            rightSum[i]=sum;
        }
        
        //calculate the max difference
        long maxDiff=Long.MIN_VALUE;
        for(int i=(N-1);i<(2*N);i++){
            long diff = leftSum[i]-rightSum[i+1];
            maxDiff=Math.max(maxDiff,diff);
        }
        return  maxDiff;
        
    }
}