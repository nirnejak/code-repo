/*
var userOne = {
    email: 'ryu@ninjas.com',
    name : 'Ryu',
    login() {
        console.log(this.email, 'has logged in');
    },
    logout() {
        console.log(this.email,'has logged out');
    }
};

userOne.name = 'Yoshi';

*/

class User {
    constructor(email, name) {
        this.email = email;
        this.name = name;
        this.score = 0;
    }
    login() {
        console.log(this.email, 'just logged in');
        return this;
    }
    logout() {
        console.log(this.email, 'just logged out');
        return this;
    }
    updateScore() {
        this.score++;
        console.log(this.email, 'score is now', this.score);
        return this;
    }
}

class Admin extends User {
    deleteUser(user) {
        users = users.filter(u => {
            return u.email != user.email
        });
    }
}

userOne = new User('ryu@ninjas.com', 'Ryu');
userTwo = new User('yoshi@ninjas.com', 'Yoshi');
var admin = new Admin('shawn@ninjas.com', 'Shaun');

var users = [userOne, userTwo, admin];
admin.deleteUser(userOne);

console.log(users);

userOne.login().updateScore().updateScore().logout();