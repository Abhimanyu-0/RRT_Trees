# RRT_Trees

- Defined a class named RRT:

execute- this function is used for compiling all the other functions of the algorithm together. 


1. Initialized all the important variables (will keep on doing so as and when I remember them)

2. Sampled a random node between 2 and 70 of size1 and added it to the mock_list 

3. A function to evaluate the sampled node(s) and print a message that says if they are within the bounds or not and then 

4. This function is used to find the distance of the node with the designated start node(which changes to the next nearest node in the next iteration). 
   - It appends the distance of the nodes in a list defined called dist-list 

5. The nearest_node function is used to find out the minimum distance in the list 
  [ a secondary question is that whether I needed to implement an altogether different function for it. 

6. This is the one that I am not really sure about, because it may avoid diretly going through the obstacles although there is a good chance that two nodes with neither of them present on the obstacle have a vector that passes through the obstacle which is not allowed.

- I instantiated the class RRT and then used the rrt.execute function.




Questions: Do I really need a node_list list? - No I don't, thats why I deleted it.


