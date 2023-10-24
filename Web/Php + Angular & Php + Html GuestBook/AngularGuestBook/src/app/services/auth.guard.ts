import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { BookService } from '../book.service';

@Injectable({
  providedIn: 'root'
})
export class authGuard implements CanActivate {
  constructor(private authService: BookService, private router: Router) {}

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

    // Check if the user is logged in or has the necessary role

    if (this.authService.getAuthStatus()) {
      // User is logged in, allow access
      return true;
    } else {
      // User is not logged in, redirect to the login page
      this.router.navigate(['/login']);
      return false;
    }
  }
}
