function User(email, name) {
    this.email = email;
    this.name = name;
    this.online = false;
    
    // It will create multiple copies of methods
    /*
    this.login = function() {
        this.online = true;
        console.log(this.email, 'has logged in');
    }
    this.logout = function() {
        this.online = false;
        console.log(this.email, 'has logged out');
    }
    */
}

User.prototype.login = function() {
    this.online = true;
    console.log(this.email, 'has logged in');
}

User.prototype.logout = function() {
    this.online = false;
    console.log(this.email, 'has logged out');
}

function Admin(...args){
    User.apply(this, args);
}

Admin.prototype = Object.create(User.prototype);
Admin.prototype.deleteUser = function(user){
    users = users.filter( u => {
        return u.email != user.email;
    })
};


var userOne = new User('ryu@ninjas.com', 'Ryu');
var userTwo = new User('yoshi@ninjas.com', 'Yoshi');
var admin = new Admin('shaun@ninjas.com','Shaun');

var users = [userOne, userTwo, admin];

console.log(admin);