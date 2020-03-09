/**
Runtime: O(n)
Where n in the number of elements in the nums vector
*/

vector<int> twoSum(vector<int>& nums, int target) {
    //Mapping the numbers that we have seen to their indices
    std::map<int, int> map;
    
    //Vector storing exactly two integers
    std::vector<int> indices;
    indices.reserve(2);

    vector<int>::iterator itr;
    for (itr = nums.begin(); itr != nums.end(); itr++) {
        //Gets the complement of the current number required to make the target
        int comp = target - *itr;

        //Gets the index
        int index = itr - nums.begin();

        //Have we seen the complement before?
        if (map.find(comp) != map.end()) {
            indices.emplace_back(map.find(comp)->second);
            indices.emplace_back(index);

            return indices;
        }

        //We last saw this number of this index
        map.insert(std::pair(*itr, index));
    }
    
    return indices;
}