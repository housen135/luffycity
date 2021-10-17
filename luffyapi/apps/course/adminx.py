

from . import models
import xadmin

xadmin.site.register(models.Course)
xadmin.site.register(models.CourseCategory)
xadmin.site.register(models.CourseChapter)
xadmin.site.register(models.CourseSection)
xadmin.site.register(models.Teacher)
# Register your models here.
