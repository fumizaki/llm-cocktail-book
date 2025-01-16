import { Card, CardContent } from "@/components/ui/card";
import type { ChatbotMessage } from "@/domain/schema";
import { MessageRole } from "@/domain/value";

type Props = {
	value: ChatbotMessage;
};

export const ChatbotMessageCard = ({ value }: Props) => {
	return (
		<Card
			className={`flex flex-col gap-4 h-fit w-full bg-gray-50 dark:bg-gray-950 border border-gray-400 dark:border-gray-600 ${value.role === MessageRole.USER ? "bg-blue-300 dark:bg-blue-300" : ""}`}
		>
			<CardContent
				className={
					`overflow-auto flex flex-col h-full gap-4 px-4 py-2 text-sm font-semibold text-slate-800 dark:text-slate-100 ${value.role === MessageRole.USER ? "text-slate-900 dark:text-slate-900" : ""}`
				}
			>
				<p className="whitespace-pre-wrap break-words">{value.content}</p>
			</CardContent>
		</Card>
	);
};
