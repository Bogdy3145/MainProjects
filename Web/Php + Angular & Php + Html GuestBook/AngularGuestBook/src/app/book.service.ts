import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, filter } from 'rxjs';
import { Book } from './book';
import { ROLE } from './components/login/login.component';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  private API: string = 'http://localhost/AngularGuestBook/PHP';

  constructor(private http: HttpClient) { }

  getBooks(filterByAuthor: string, filterByTitle: string, page: number = 1): Observable<Book[]> {
    const params = new HttpParams()
      .set('filter_by_author', filterByAuthor)
      .set('filter_by_title', filterByTitle)
      .set('page', page.toString());

    const url = `${this.API}/BrowseBook.php`;
    return this.http.get<Book[]>(url, { params });
  }

  getAllBooks(): Observable<Book[]>{
    const url = `${this.API}/GetBookList.php`;
    return this.http.get<Book[]>(url);
  }

  addBook(book: Book): Observable<any> {
  
    return this.http.post(`${this.API}/AddBook.php`, book);
  }

  deleteBook(BookName: string): Observable<any> {
    return this.http.delete(`${this.API}/DeleteBook.php?BookName=${BookName}`);
  }


  updateBook(book: Book): Observable<any> {
    return this.http.put(`${this.API}/UpdateBookButton.php`, book);
  }

  login(username: string, password: string): Observable<any> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    
    return this.http.post(`${this.API}/login.php`, formData);
  }

  getAuthStatus(){
    if (ROLE.role == "admin")
      return true;
    return false;
  }

 
}
