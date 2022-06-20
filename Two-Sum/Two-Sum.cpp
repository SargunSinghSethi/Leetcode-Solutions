class Solution
{
public:
  vector<int> twoSum(vector<int>& nums, int target)
  {
    vector <int> ans;
    std::unordered_map <int,int> mpp;
    
    for(int i = 0; i < nums.size(); i++)
    {
      int comp = target - nums[i];
      if(mpp.find(comp) != mpp.end())
      {
        ans.push_back(mpp[comp]);
        ans.push_back(i);
        return ans;
      }
      map[nums[i]] = i;
    }
    return ans;
  }
};
