// Solution 2: more memory efficient
class ProductOfNumbers {
public:
    vector<int> products{1};

    ProductOfNumbers() = default;
    
    void add(int num) {
        if (num == 0) {
            products.assign(1, 1);
        } else {
            products.push_back(num * products.back());
        }
    }
    
    int getProduct(int k) {
        int n = products.size();
        if (k >= n) {
            return 0;
        }

        return products.back() / products[n - 1 - k];
    }
};

// Solution 1
// class ProductOfNumbers {
// public:
//     vector<int> products{1};
    
//     // We only store the maximum indice zero
//     int zero{ -1 };

//     ProductOfNumbers() = default;
    
//     void add(int num) {
//         if (num == 0) {
//             zero = size() - 1;
//             products.push_back(1);
//         } else {
//             products.push_back(num * products[size() - 1]);
//         }
//     }
    
//     int getProduct(int k) {
//         if (zero >= static_cast<int>(size()) - 1 - k) {
//             return 0;
//         }

//         return products[size() - 1] / products[size() - 1 - k];
//     }

//     size_t size() const noexcept {
//         return products.size();
//     }
// };

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */