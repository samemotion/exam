 renderElement: function() {

        var self = this;

        this._super();

        this.$('.pay').click(function(){

            var order = self.pos.get_order();

            ////  incluye control de cantidades = 0   Omar 14.05.2020

            var has_cero =_.every(order.orderlines.models, function (line) {

                return line.quantity > 0;

            });

            if (!has_cero) {

                alert(_t(

                    'Error en el ingreso de productos. ' +

                    'Cantidad = cero. Debe modificar o eliminar linea(s)'

                ));

                return;

            }

 

            var has_cero =_.every(order.orderlines.models, function (line) {

                return line.list_price > 0;

            });

            if (!has_cero) {

                alert(_t(

                    'Error en el ingreso de productos. ' +

                    'Precio Valor cero. Debe modificar o eliminar linea(s)'

                ));

                return;

            }

 

            ///

            var has_valid_product_lot = _.every(order.orderlines.models, function(line){

                return line.has_valid_product_lot();

            });

            if(!has_valid_product_lot){

                self.gui.show_popup('confirm',{

                    'title': _t('Empty Serial/Lot Number'),

                    'body':  _t('One or more product(s) required serial/lot number.'),

                    confirm: function(){

                        self.gui.show_screen('payment');

                    },

                });

            }else{

                self.gui.show_screen('payment');

            }

        });

        this.$('.set-customer').click(function(){

            self.gui.show_screen('clientlist');

        });

    }

});