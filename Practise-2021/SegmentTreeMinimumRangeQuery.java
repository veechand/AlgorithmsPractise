public class SegmentTreeMinimumRangeQuery {

    /**
     * Creates a new segment tree based off input array.
     */
    public int[] createSegmentTree(int input[]){
        //if input len is pow of 2 then size of 
        //segment tree is 2*len - 1, otherwise
        //size of segment tree is next (pow of 2 for len)*2 - 1.
        int nextPowOfTwo = 4;
        int segmentTree[] = new int[nextPowOfTwo*2 -1];
        System.out.println(segmentTree.length);
        for(int i=0; i < segmentTree.length; i++){
            segmentTree[i] = Integer.MAX_VALUE;
        }
        constructMinSegmentTree(segmentTree, input, 0, input.length - 1, 0);
        return segmentTree;
        
    }


    private void constructMinSegmentTree(int segmentTree[], int input[], int low, int high,int pos){
        if(low == high){
            segmentTree[pos] = input[low];
            return;
        }
        int mid = (low + high)/2;
        System.out.println("mid="+mid+" start="+low+" end="+high+"pos="+pos);
        constructMinSegmentTree(segmentTree, input, low, mid, 2 * pos + 1);
        constructMinSegmentTree(segmentTree, input, mid + 1, high, 2 * pos + 2);
        segmentTree[pos] = Math.min(segmentTree[2*pos+1], segmentTree[2*pos+2]);
    }

    private int rangeMinimumQuery(int segmentTree[],int low,int high,int qlow,int qhigh,int pos){
        if(qlow <= low && qhigh >= high){
            return segmentTree[pos];
        }
        if(qlow > high || qhigh < low){
            return Integer.MAX_VALUE;
        }
        int mid = (low+high)/2;
        return Math.min(rangeMinimumQuery(segmentTree, low, mid, qlow, qhigh, 2 * pos + 1),
                rangeMinimumQuery(segmentTree, mid + 1, high, qlow, qhigh, 2 * pos + 2));
    }

   
 
    public static void main(String args[]){
        SegmentTreeMinimumRangeQuery st = new SegmentTreeMinimumRangeQuery();

        int input[] = {1,2,3,4};
        int segTree[] = st.createSegmentTree(input);

    }
}
