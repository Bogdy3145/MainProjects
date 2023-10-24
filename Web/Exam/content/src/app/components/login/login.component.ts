import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ContentService } from 'src/app/content.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private router: Router, private contentService: ContentService) {}

  login() {
    this.contentService.login(this.username, this.password).subscribe(
      (response: any) => {
        // Check the response for successful login
        if (response) {
          // Redirect to addbook.html or perform any other actions upon successful login
          //alert("Wp");
          localStorage.setItem('userid', response.userid);
          if (response.role == "creator"){
            localStorage.setItem('role',"creator");
            
            //ROLE.role="admin";
          }
          else{
            //ROLE.role="user";
            localStorage.setItem('role',"reader");

          }
          console.log(localStorage.getItem('role'));
          this.router.navigate(['/content']);
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
