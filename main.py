from notion_client.client import Client, ClientOptions
import vcr

c = Client(
    options=ClientOptions(auth="secret_VYG3FR8A36oAJKc57xs4FdaRRqvl5pRRrYOC1FdvNjK")
)

with vcr.use_cassette("tests/fixtures/vcr_cassettes/DATABASES_LIST_0.yaml"):
    databases_list_data = c.databases.list().json()
    database = databases_list_data["results"][0]
    database_id = database["id"]

with vcr.use_cassette("tests/fixtures/vcr_cassettes/USERS_LIST_0.yaml"):
    c.users.list().json()

with vcr.use_cassette("tests/fixtures/vcr_cassettes/DATABASES_RETRIEVE_0.yaml"):
    c.databases.retrieve(database_id=database_id)

    # with vcr.use_cassette("tests/fixtures/vcr_cassettes/DATABASES_QUERY_0.yaml"):
    #     data = c.databases.query(
    #         database_id=database_id,
    #         **{
    #             "filter": {
    #                 "or": [
    #                     {"property": "Status", "select": {"equals": "In progress"}},
    #                     {"property": "Priority", "number": {"equals": 1}},
    #                 ]
    #             }
    #         }
    #     )

    # with vcr.use_cassette("tests/fixtures/vcr_cassettes/PAGES_"):
c.pages.create(
    **{
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {"title": [{"text": {"content": "Tuscan Kale"}}]},
            "Description": {
                "rich_text": [{"text": {"content": "A dark green leafy vegetable"}}]
            },
            "Food group": {"select": {"name": "Vegetable"}},
            "Price": {"number": 2.5},
        },
        "children": [
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
                },
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                                "link": {
                                    "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                                },
                            },
                        }
                    ]
                },
            },
        ],
    }
)
