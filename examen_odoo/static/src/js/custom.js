odoo.define('js.custom_button', function (require) {
    "use strict";
    var core = require('web.core');
    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');
    
    
    
    var CustomButton2 = screens.PaymentScreenWidget.extend({
        template: 'CustomButton2',
    
        button_click: function(){
    
        var self = this;
        self.custom_function();
        
        },
    
        custom_function: function(){
            console.log('Boton');
        }
    
    });
    
    screens.define_action_button({
        'name': 'custom_button',
        'widget': CustomButton2,
    });
    
    
    
    
    });