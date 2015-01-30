BEGIN;
CREATE TABLE "bookmark_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE);
CREATE TABLE "bookmark_page" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(128) NOT NULL, "url" varchar(200) NOT NULL, "views" integer NOT NULL, "category_id" integer NOT NULL REFERENCES "bookmark_category" ("id"));
CREATE INDEX "bookmark_page_b583a629" ON "bookmark_page" ("category_id");

COMMIT;
