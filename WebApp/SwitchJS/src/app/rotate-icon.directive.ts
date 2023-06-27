import { keyframes } from '@angular/animations';
import { Directive, ElementRef, HostListener } from '@angular/core';

@Directive({
  selector: '[appRotateIcon]'
})
export class RotateIconDirective {
  rotation = 0;
  constructor(private el: ElementRef) { }

  @HostListener('click') onClick() {
    let rotateIcon = this.el.nativeElement.querySelector('.rotate-icon');
    if (!rotateIcon.parentElement.classList.contains('disabled'))
      rotateIcon.style.transform = `rotate(${this.rotation+=360}deg)`;
  }
}
