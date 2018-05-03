
class StoreRouter:
    """
    A router to control operations in store app
    """
    def db_for_read(self, model, **hints):
        return 'store'

    def db_for_write(self, model, **hints):
        return 'store'
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
