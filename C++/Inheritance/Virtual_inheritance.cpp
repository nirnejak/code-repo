#include <iostream>
using namespace std;

class STUDENT{
	protected:
		int rollNo;
	public:
		void getNo(int x){
			rollNo=x;
		}
		void putNo(){
			cout<<endl<<rollNo;
		}
};

class SCORE : virtual public STUDENT{
	protected:
		float score;
	public:
		void getScore(float x){
			score=x;
		}
		void putScore(){
			cout<<endl<<score;
		}
};

class TEST : public virtual STUDENT{
	protected:
		float sub1,sub2;
	public:
		void getMarks(float p,float q){
			sub1=p;
			sub2=q;
		}
		void putMarks(){
			cout<<endl<<sub1;
			cout<<endl<<sub2;
		}
};

class RESULT : public TEST, public SCORE{
		float total;
	public:
		void display(){
			total=sub1+sub2+score;
			putNo();
			putMarks();
			putScore();
			cout<<endl<<total;
		}
};

int main(){
	RESULT obj;
	obj.getNo(132567);
	obj.getMarks(88,93);
	obj.getScore(93);
	obj.display();
	return 0;
}