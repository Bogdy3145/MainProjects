import { Component } from '@angular/core';
import { Book } from 'src/app/book';
import { BookService } from 'src/app/book.service';
import { ROLE } from '../login/login.component';

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent {
  books: Book[] = [];

  constructor(private bookService: BookService) {}

  ngOnInit() {
    this.getBooks();
  }

  getBooks() {
    this.bookService.getAllBooks().subscribe(
      (data: Book[]) => {
        this.books = data;
      }
    );
  }

  deleteEntry(bookTitle: string) {
    if (ROLE.role == "admin"){
    if (confirm('Are you sure you want to delete the entry with title "' + bookTitle + '"?')) {
      this.bookService.deleteBook(bookTitle).subscribe(
        (response: any) => {
          alert(response.message); // Display the response message
          this.getBooks(); // Refresh the book list after successful deletion
        }
      );
    }
  }
  else{
    alert("No rights!");
  }
  }
}
