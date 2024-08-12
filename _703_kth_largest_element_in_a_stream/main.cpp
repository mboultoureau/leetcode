class KthLargest {
public:
    KthLargest(int k, vector<int>& nums): m_K(k) {
        for (int n : nums)
        {
            m_Nums.push(n);
            if (m_Nums.size() > m_K)
            {
                m_Nums.pop();
            }
        }
    }
    
    int add(int val) {
        m_Nums.push(val);
        if (m_Nums.size() > m_K)
        {
            m_Nums.pop();
        }
        return m_Nums.top();
    }
private:
    int m_K;
    priority_queue<int, vector<int>, greater<int>> m_Nums;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */