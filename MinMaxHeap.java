package ex0.algo;

import java.util.PriorityQueue;

public interface MinMaxHeap {
    PriorityQueue<Integer> Heap = new PriorityQueue<>();
    public void add(int a);
    public void delete();
    public Integer peek();
    public boolean isEmpty();
    public int size();

}
