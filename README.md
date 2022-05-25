# RRT_Trees
## This is an original implementation of the rapidly expanding random trees algorithm.


NOTE: 
1. The obstacle detection and avoidance function needs work.
2. Need to plot the final points.









## A function by function summary of the code.
- Defined a class named RRT:

execute- this function is used for compiling all the other functions of the algorithm together. 


1. Initialized all the important variables (will keep on doing so as and when I remember them)

2. Sampled a random node between 10 and 90 of size1 and added it to the mock_list 

3. A function to evaluate the sampled node(s) and print a message that says if they are within the bounds or not.

4. This is the collision avoidance function.

5. This function is used to find the distance of the node with the designated start node(which changes to the next nearest node in the next iteration). 
   - It appends the distance of the nodes in a list defined called dist-list 

6. The nearest_node function is used to find out the minimum distance in the list 
  [ a secondary question is that whether I needed to implement an altogether different function for it. 



- I instantiated the class RRT and then used the rrt.execute function.











