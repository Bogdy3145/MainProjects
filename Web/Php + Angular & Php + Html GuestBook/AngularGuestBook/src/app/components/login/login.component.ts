import { Component } from '@angular/core';
import { BookService } from 'src/app/book.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private router: Router, private bookService: BookService) {}

  login() {
    this.bookService.login(this.username, this.password).subscribe(
      (response: any) => {
        // Check the response for successful login
        if (response) {
          // Redirect to addbook.html or perform any other actions upon successful login
          //alert("Wp");
          if (response == "admin"){
            ROLE.role="admin";
          }
          else{
            ROLE.role="user";
          }

          this.router.navigate(['/addbook']);
        } else {
          alert("unlucky");


        }
      }
    );

    // Reset the form fields after login
    this.username = '';
    this.password = '';
  }
}


export const ROLE = {
  role: ""
}
