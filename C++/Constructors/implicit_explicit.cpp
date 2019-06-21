#include <iostream>
using namespace std;

class TEST{
    private:
        int a,b;
    public:
        TEST(int x, int y);
        void showData();
};

int main(){
    TEST obj1 = TEST(7,9),obj2(3,9);    //explicit and implicit
    obj1.showData();
    obj2.showData();
    return 0;
}

//constructor definition
TEST::TEST(int x, int y){
    this.a=x;
    this.b=y;
}

void TEST::showData(){
    cout<<a<<endl<<b<<endl;
}