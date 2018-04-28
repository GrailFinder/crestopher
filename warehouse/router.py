

class WarehouseRouter:
    """
    A router to control operations in warehouse app
    """
    def db_for_read(self, model, **hints):
        if model.meta.app_label == 'warehouse':
            return 'warehouse_db'

    def db_for_write(self, model, **hints):
        if model.meta.app_label == 'warehouse':
            return 'warehouse_db'
    
    def allow_migrate(self, model, **hints):
        if model.meta.app_label == 'warehouse':
            return 'warehouse_db'
