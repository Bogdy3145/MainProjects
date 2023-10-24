import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, filter } from 'rxjs';
import { User } from './User';
import { Content } from './Content';

@Injectable({
    providedIn: 'root'
  })
  export class ContentService {
  
    private API: string = 'http://localhost/Exam/content/PHP';
    constructor(private http: HttpClient) { }

    getAllContent(){
        const url = `${this.API}/GetContent.php`;
        return this.http.get<Content[]>(url);
    }

    login(username: string, password: string): Observable<any> {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);
        
        return this.http.post(`${this.API}/login.php`, formData);
      }

    addContent(content: Content): Observable<any> {
  
        return this.http.post(`${this.API}/AddContent.php`, content);
    }  
  }
