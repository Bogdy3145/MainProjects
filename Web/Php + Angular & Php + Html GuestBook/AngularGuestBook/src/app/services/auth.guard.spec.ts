import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { authGuard } from './auth.guard';
import { BookService } from '../book.service';

describe('authGuard', () => {
  let guard: authGuard;
  let mockAuthService: jasmine.SpyObj<BookService>;
  let mockRouter: jasmine.SpyObj<Router>;
  let mockActivatedRouteSnapshot: ActivatedRouteSnapshot;
  let mockRouterStateSnapshot: RouterStateSnapshot;

  beforeEach(() => {
    mockAuthService = jasmine.createSpyObj('BookService', ['getAuthStatus']);
    mockRouter = jasmine.createSpyObj('Router', ['navigate']);

    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      providers: [
        { provide: BookService, useValue: mockAuthService },
        { provide: Router, useValue: mockRouter }
      ]
    });

    guard = TestBed.inject(authGuard);
    mockActivatedRouteSnapshot = jasmine.createSpyObj<ActivatedRouteSnapshot>('ActivatedRouteSnapshot', [], { data: {} });
    mockRouterStateSnapshot = jasmine.createSpyObj<RouterStateSnapshot>('RouterStateSnapshot', [], { url: '/deletebook' });
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });

  it('should allow access if user is logged in', () => {
    mockAuthService.getAuthStatus.and.returnValue(true);

    const result = guard.canActivate(mockActivatedRouteSnapshot, mockRouterStateSnapshot);

    expect(result).toBeTrue();
    expect(mockAuthService.getAuthStatus).toHaveBeenCalled();
    expect(mockRouter.navigate).not.toHaveBeenCalled();
  });

  it('should redirect to login page if user is not logged in', () => {
    mockAuthService.getAuthStatus.and.returnValue(false);

    const result = guard.canActivate(mockActivatedRouteSnapshot, mockRouterStateSnapshot);

    expect(result).toBeFalse();
    expect(mockAuthService.getAuthStatus).toHaveBeenCalled();
    expect(mockRouter.navigate).toHaveBeenCalledWith(['/login']);
  });
});
