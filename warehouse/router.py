
class WarehouseRouter:
    """
    A router to control operations in warehouse app
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'warehouse':
            return 'warehouse'
        else:
            return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'warehouse':
            return 'warehouse'
        else:
            return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'warehouse':
            return db == 'warehouse'
        return None
