import Link from "next/link";
import { Card } from "@/components/ui/card";
import { Book, BookPlus } from "lucide-react";
import { EditChatbotIndexDialog } from "@/components/chatbot/dialog/edit-chatbot-index-dialog";
import { DeleteChatbotIndexDialog } from "@/components/chatbot/dialog/delete-chatbot-index-dialog";
import type { ChatbotIndex } from "@/domain/schema";

export const ChatbotIndexCard = ({
	value,
}: {
	value: ChatbotIndex;
}) => {
	return (
		<Card
			className={
				"relative w-full h-36 flex flex-col gap-1.5 py-3.5 pl-3.5 pr-1.5 cursor-pointer overflow-hidden border-blue-800 bg-blue-500/25 hover:bg-blue-700/25"
			}
		>
			<div className={"flex flex-1 flex-col flex-start gap-1.5"}>
			<div className={"flex gap-1.5"}>
					<BookPlus />
				</div>
				<div
					className={
						"font-tiempos line-clamp-1 overflow-hidden text-base md:line-clamp-2 md:h-12 md:pr-2"
					}
				>
					{value.title}
				</div>
			</div>
			<div className={"absolute z-20 right-2 bottom-2 flex"}>
				<EditChatbotIndexDialog value={value} />
				<DeleteChatbotIndexDialog value={value} />
			</div>
		</Card>
	);
};
