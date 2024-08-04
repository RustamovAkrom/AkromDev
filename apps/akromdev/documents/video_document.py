from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from apps.akromdev.models import Video

video_model_index = Index("videos")


video_model_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@registry.register_document
@video_model_index.doc_type
class VideoModelDocument(Document):
    class Django:
        model = Video
        fields = [
            "title",
        ]