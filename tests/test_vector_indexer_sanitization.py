from ingestion.vector_indexer import VectorIndexer


class DummyChunk:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata or {}


def test_sanitize_chunks_normalizes_non_string_content():
    indexer = VectorIndexer()
    chunks = [
        DummyChunk(["hello", "world"], {}),
        DummyChunk({"title": "doc", "body": "hello there"}, {}),
        DummyChunk(None, {}),
        DummyChunk("  keep  this   text  ", {}),
    ]

    cleaned = indexer._sanitize_chunks(chunks)

    assert [chunk.page_content for chunk in cleaned] == [
        "hello world",
        "doc hello there",
        "keep this text",
    ]
