import { Pipe, PipeTransform } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Pipe({
  name: 'searchHighlight'
})
export class SearchHighlightPipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer) {}
  transform(value: any, args: any): SafeHtml {
    if( !args ) {
      return value;
    }
    const re = new RegExp(args, 'igm');
    value = value.replace(re, '<mark class="highlight">$&</mark>');
    return this.sanitizer.bypassSecurityTrustHtml(value);
  }

}
