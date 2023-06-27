import { Component, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { state, animate, style, transition, trigger } from '@angular/animations';

@Component({
  selector: 'app-csv-modal',
  templateUrl: './csv-modal.component.html',
  styleUrls: ['./csv-modal.component.css'],
  animations: [
    trigger('openClose', [
      state('open', style({
		height: '*'
      })),
      state('closed', style({
		height: '0'
      })),
      transition('open => closed', [
        animate('0.1s')
      ]),
      transition('closed => open', [
        animate('0.1s')
      ]),
    ]),
  ],
  host: {
    '(document:keydown)': 'onEnter($event)'
  }
})

export class CsvModalComponent {
	@Input() devices: [any];
	showAdvanced = false;

	deviceAttr = {
		'Hostname':{ selector: 'hostname', csvInclude: true },
		'Make':{ selector: 'make', csvInclude: true },
		'Model':{ selector: 'model', csvInclude: true },
		'Serial':{ selector: 'serial', csvInclude: true },
		'Firmware':{ selector: 'firmware', csvInclude: true },
		'FIPS Status':{ selector: 'fips', csvInclude: true },
		'All IPs':{ selector: 'ip_addresses', csvInclude: false },
		'Last Updated':{ selector: 'updated', csvInclude: false },
		'Uptime':{ selector: 'uptime', csvInclude: false },
		'Active User Ports':{ selector: 'users', csvInclude: false },
		'Base MAC':{ selector: 'baseMAC', csvInclude: false },
		'Reachability':{ selector: 'status', csvInclude: false }
	}
	orderedHeaderTemplate = [
		'Hostname',
		'Make',
		'Model',
		'Serial',
		'Firmware',
		'FIPS Status',
		'All IPs',
		'Last Updated',
		'Uptime',
		'Active User Ports',
		'Base MAC',
		'Reachability'
	]
	constructor(public activeModal: NgbActiveModal) {}

	onEnter(event: any) {
		if (event.key === 'Enter') {
			this.exportCSV()
		}
	}
	toggleAdvanced() {
		this.showAdvanced = !this.showAdvanced;
	}
	updateExportAttr(attr, csvInclude) {
		this.deviceAttr[attr].csvInclude = csvInclude;
	}
	exportCSV() {
		let header = ['IP Address'];

		this.orderedHeaderTemplate.forEach(col => {
			if (this.deviceAttr[col].csvInclude)
				header.push(col);
		});
		
		let csv = 'data:text/csv;charset=utf-8,';
		csv+= header.join(',') + '\r\n'
		this.devices.forEach(device => {
			let row = []
			row.push(device.scan_ip);
			header.forEach(col => {
				if ( col === 'IP Address' )
					return device.scan_ip;

				let exportAttr = this.deviceAttr[col].selector;
				if ( exportAttr === 'ip_addresses' ) 
					return row.push(Object.keys(device.ip_addresses).join(','));
				return row.push(String(device[exportAttr]))
			});
			csv+= '"' + row.join('","') + '"\r\n' // added extra double quotes to escape commas in list elements
		});

		let csvURI = encodeURI(csv);
		var link = document.createElement("a");
		link.setAttribute("href", csvURI);
		link.setAttribute("download", "networklist.csv");
		document.body.appendChild(link); // Required for Firefox
		link.click(); // This will download the data file named "networklist.csv"
		this.activeModal.close()
	  }
}
