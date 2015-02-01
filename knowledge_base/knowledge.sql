BEGIN;
CREATE TABLE "knowledge_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "added" datetime NOT NULL, "lastchanged" datetime NOT NULL, "title" varchar(255) NOT NULL, "slug" varchar(50) NOT NULL UNIQUE);
CREATE TABLE "knowledge_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "added" datetime NOT NULL, "lastchanged" datetime NOT NULL, "alert" bool NOT NULL, "name" varchar(64) NULL, "email" varchar(75) NULL, "title" varchar(255) NOT NULL, "body" text NULL, "status" varchar(32) NOT NULL, "locked" bool NOT NULL, "user_id" integer NULL REFERENCES "auth_user" ("id"));
CREATE TABLE "knowledge_question_categories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_id" integer NOT NULL REFERENCES "knowledge_question" ("id"), "category_id" integer NOT NULL REFERENCES "knowledge_category" ("id"), UNIQUE ("question_id", "category_id"));
CREATE TABLE "knowledge_response" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "added" datetime NOT NULL, "lastchanged" datetime NOT NULL, "alert" bool NOT NULL, "name" varchar(64) NULL, "email" varchar(75) NULL, "body" text NULL, "status" varchar(32) NOT NULL, "accepted" bool NOT NULL, "question_id" integer NOT NULL REFERENCES "knowledge_question" ("id"), "user_id" integer NULL REFERENCES "auth_user" ("id"));
CREATE INDEX "knowledge_question_9acb4454" ON "knowledge_question" ("status");
CREATE INDEX "knowledge_question_e8701ad4" ON "knowledge_question" ("user_id");
CREATE INDEX "knowledge_question_categories_7aa0f6ee" ON "knowledge_question_categories" ("question_id");
CREATE INDEX "knowledge_question_categories_b583a629" ON "knowledge_question_categories" ("category_id");
CREATE INDEX "knowledge_response_9acb4454" ON "knowledge_response" ("status");
CREATE INDEX "knowledge_response_7aa0f6ee" ON "knowledge_response" ("question_id");
CREATE INDEX "knowledge_response_e8701ad4" ON "knowledge_response" ("user_id");

COMMIT;
