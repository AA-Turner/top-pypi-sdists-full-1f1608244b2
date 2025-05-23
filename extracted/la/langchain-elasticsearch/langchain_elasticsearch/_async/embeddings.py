from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers.vectorstore import AsyncEmbeddingService
from langchain_core.embeddings import Embeddings
from langchain_core.utils import get_from_env

if TYPE_CHECKING:
    from elasticsearch._async.client.ml import MlClient


class AsyncElasticsearchEmbeddings(Embeddings):
    """Elasticsearch embedding models.

    This class provides an interface to generate embeddings using a model deployed
    in an Elasticsearch cluster. It requires an Elasticsearch connection object
    and the model_id of the model deployed in the cluster.

    In Elasticsearch you need to have an embedding model loaded and deployed.
    - https://www.elastic.co/guide/en/elasticsearch/reference/current/infer-trained-model.html
    - https://www.elastic.co/guide/en/machine-learning/current/ml-nlp-deploy-models.html

    For synchronous applications, use the `ElasticsearchEmbeddings` class.
    For asyhchronous applications, use the `AsyncElasticsearchEmbeddings` class.
    """  # noqa: E501

    def __init__(
        self,
        client: MlClient,
        model_id: str,
        *,
        input_field: str = "text_field",
    ):
        """
        Initialize the ElasticsearchEmbeddings instance.

        Args:
            client (MlClient): An Elasticsearch ML client object.
            model_id (str): The model_id of the model deployed in the Elasticsearch
                cluster.
            input_field (str): The name of the key for the input text field in the
                document. Defaults to 'text_field'.
        """
        self.client = client
        self.model_id = model_id
        self.input_field = input_field

    @classmethod
    def from_credentials(
        cls,
        model_id: str,
        *,
        es_cloud_id: Optional[str] = None,
        es_api_key: Optional[str] = None,
        input_field: str = "text_field",
    ) -> AsyncElasticsearchEmbeddings:
        """Instantiate embeddings from Elasticsearch credentials.

        Args:
            model_id (str): The model_id of the model deployed in the Elasticsearch
                cluster.
            input_field (str): The name of the key for the input text field in the
                document. Defaults to 'text_field'.
            es_cloud_id: (str, optional): The Elasticsearch cloud ID to connect to.
            es_user: (str, optional): Elasticsearch username.
            es_password: (str, optional): Elasticsearch password.

        Example:
            .. code-block:: python

                from langchain_elasticserach.embeddings import ElasticsearchEmbeddings

                # Define the model ID and input field name (if different from default)
                model_id = "your_model_id"
                # Optional, only if different from 'text_field'
                input_field = "your_input_field"

                # Credentials can be passed in two ways. Either set the env vars
                # ES_CLOUD_ID, ES_USER, ES_PASSWORD and they will be automatically
                # pulled in, or pass them in directly as kwargs.
                embeddings = ElasticsearchEmbeddings.from_credentials(
                    model_id,
                    input_field=input_field,
                    # es_cloud_id="foo",
                    # es_user="bar",
                    # es_password="baz",
                )

                documents = [
                    "This is an example document.",
                    "Another example document to generate embeddings for.",
                ]
                embeddings_generator.embed_documents(documents)
        """
        from elasticsearch._async.client.ml import MlClient

        es_cloud_id = es_cloud_id or get_from_env("es_cloud_id", "ES_CLOUD_ID")
        es_api_key = es_api_key or get_from_env("es_api_key", "ES_API_KEY")

        # Connect to Elasticsearch
        es_connection = AsyncElasticsearch(cloud_id=es_cloud_id, api_key=es_api_key)
        client = MlClient(es_connection)
        return cls(client, model_id, input_field=input_field)

    @classmethod
    def from_es_connection(
        cls,
        model_id: str,
        es_connection: AsyncElasticsearch,
        input_field: str = "text_field",
    ) -> AsyncElasticsearchEmbeddings:
        """
        Instantiate embeddings from an existing Elasticsearch connection.

        This method provides a way to create an instance of the ElasticsearchEmbeddings
        class using an existing Elasticsearch connection. The connection object is used
        to create an MlClient, which is then used to initialize the
        ElasticsearchEmbeddings instance.

        Args:
        model_id (str): The model_id of the model deployed in the Elasticsearch cluster.
        es_connection (elasticsearch.Elasticsearch): An existing Elasticsearch
        connection object. input_field (str, optional): The name of the key for the
        input text field in the document. Defaults to 'text_field'.

        Returns:
        ElasticsearchEmbeddings: An instance of the ElasticsearchEmbeddings class.

        Example:
            .. code-block:: python

                from elasticsearch import Elasticsearch

                from langchain_elasticsearch.embeddings import ElasticsearchEmbeddings

                # Define the model ID and input field name (if different from default)
                model_id = "your_model_id"
                # Optional, only if different from 'text_field'
                input_field = "your_input_field"

                # Create Elasticsearch connection
                es_connection = Elasticsearch(
                    hosts=["localhost:9200"], http_auth=("user", "password")
                )

                # Instantiate ElasticsearchEmbeddings using the existing connection
                embeddings = ElasticsearchEmbeddings.from_es_connection(
                    model_id,
                    es_connection,
                    input_field=input_field,
                )

                documents = [
                    "This is an example document.",
                    "Another example document to generate embeddings for.",
                ]
                embeddings_generator.embed_documents(documents)
        """
        from elasticsearch._async.client.ml import MlClient

        # Create an MlClient from the given Elasticsearch connection
        client = MlClient(es_connection)

        # Return a new instance of the ElasticsearchEmbeddings class with
        # the MlClient, model_id, and input_field
        return cls(client, model_id, input_field=input_field)

    async def _embedding_func(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for the given texts using the Elasticsearch model.

        Args:
            texts (List[str]): A list of text strings to generate embeddings for.

        Returns:
            List[List[float]]: A list of embeddings, one for each text in the input
                list.
        """
        response = await self.client.infer_trained_model(
            model_id=self.model_id, docs=[{self.input_field: text} for text in texts]
        )

        embeddings = [doc["predicted_value"] for doc in response["inference_results"]]
        return embeddings

    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of documents.

        Args:
            texts (List[str]): A list of document text strings to generate embeddings
                for.

        Returns:
            List[List[float]]: A list of embeddings, one for each document in the input
                list.
        """
        return await self._embedding_func(texts)

    async def aembed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query text.

        Args:
            text (str): The query text to generate an embedding for.

        Returns:
            List[float]: The embedding for the input query text.
        """
        return (await self._embedding_func([text]))[0]


class AsyncEmbeddingServiceAdapter(AsyncEmbeddingService):
    """
    Adapter for LangChain Embeddings to support the EmbeddingService interface from
    elasticsearch.helpers.vectorstore.
    """

    def __init__(self, langchain_embeddings: Embeddings):
        self._langchain_embeddings = langchain_embeddings

    def __eq__(self, other):  # type: ignore[no-untyped-def]
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    async def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of documents.

        Args:
            texts (List[str]): A list of document text strings to generate embeddings
                for.

        Returns:
            List[List[float]]: A list of embeddings, one for each document in the input
                list.
        """
        return await self._langchain_embeddings.aembed_documents(texts)

    async def embed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query text.

        Args:
            text (str): The query text to generate an embedding for.

        Returns:
            List[float]: The embedding for the input query text.
        """
        return await self._langchain_embeddings.aembed_query(text)
