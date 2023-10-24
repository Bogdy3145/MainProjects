import { Component } from '@angular/core';
import { Book } from 'src/app/book'; 
import { BookService } from 'src/app/book.service';
import { Location } from '@angular/common';
import { ROLE } from '../login/login.component';


@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent {
  books: Book[] = [];
  selectedBook: Book = { Title: '', Author: '', Comment: '', Date: new Date() }; // Define the selectedBook property

  constructor(private bookService: BookService, private location: Location) {}

  ngOnInit() {
    this.getBooks();
  }

  getBooks() {
    this.bookService.getAllBooks().subscribe(
      (data: any) => {
        this.books = data;
        console.log(this.books);
      }
    );
  }
  

  selectBook(book: Book) {
    this.selectedBook = { ...book }; // Copy the selected book into the selectedBook property
  }

  updateEntry() {
    if (ROLE.role=="admin"){
      // Call the bookService method to update the entry and handle the response
      this.bookService.updateBook(this.selectedBook).subscribe(
        (response) => {
          console.log('Update successful:', response);
          this.getBooks();
          //this.location.go(this.location.path()); // Reload the current URL
          //window.location.reload(); // Reload the entire page
          // Handle success, e.g., show a success message or navigate to another page
        }
        
      );
    }
    else{
      console.log('Failed! No rights.');
      //alert("No rights!");
      //this.location.go(this.location.path());
    }
  }

  confirmUpdate() {
    // Add any confirmation logic before calling the updateEntry() method
    if (confirm('Are you sure you want to update this entry?')) {
      this.updateEntry();
    } else {
      // Handle cancellation, e.g., show a message or perform fallback action
    }
  }

}
